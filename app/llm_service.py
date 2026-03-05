from openai import OpenAI

from app.config import settings

VALID_SEVERITIES = {"low", "medium", "high", "critical"}


class SeverityAnalyzer:
    def __init__(self):
        self.model = settings.llm_model
        self.fallback = settings.fallback_severity
        self.provider = settings.llm_provider.lower()
        self.client = OpenAI(api_key=settings.llm_api_key) if settings.llm_api_key else None

    def _normalize(self, severity: str) -> str:
        clean = severity.strip().lower()
        return clean if clean in VALID_SEVERITIES else self.fallback

    def predict(self, title: str, description: str) -> tuple[str, str]:
        if self.provider != "openai" or not self.client:
            rule_based = self._rule_based_prediction(title, description)
            return rule_based, "rule-based-fallback"

        prompt = (
            "Classify bug severity as exactly one word: low, medium, high, or critical. "
            "No explanation.\n"
            f"Title: {title}\n"
            f"Description: {description}"
        )

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
            temperature=0,
            max_output_tokens=5,
        )

        text = response.output_text or ""
        return self._normalize(text), self.model

    def _rule_based_prediction(self, title: str, description: str) -> str:
        text = f"{title} {description}".lower()

        critical_markers = ["data loss", "security", "payment failure", "crash loop", "production down"]
        high_markers = ["crash", "exception", "cannot login", "blocked", "500"]
        low_markers = ["typo", "alignment", "cosmetic", "minor ui"]

        if any(marker in text for marker in critical_markers):
            return "critical"
        if any(marker in text for marker in high_markers):
            return "high"
        if any(marker in text for marker in low_markers):
            return "low"
        return "medium"
