"""Tests for AudioIntelligencePlatform."""
from src.core import AudioIntelligencePlatform
def test_init(): assert AudioIntelligencePlatform().get_stats()["ops"] == 0
def test_op(): c = AudioIntelligencePlatform(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = AudioIntelligencePlatform(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = AudioIntelligencePlatform(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = AudioIntelligencePlatform(); r = c.process(); assert r["service"] == "audio-intelligence-platform"
