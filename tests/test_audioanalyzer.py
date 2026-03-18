"""Tests for AudioAnalyzer."""
import pytest
from src.audioanalyzer import AudioAnalyzer

def test_init():
    obj = AudioAnalyzer()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = AudioAnalyzer()
    result = obj.transcribe(input="test")
    assert result["processed"] is True
    assert result["operation"] == "transcribe"

def test_multiple_ops():
    obj = AudioAnalyzer()
    for m in ['transcribe', 'detect_speakers', 'analyze_sentiment']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = AudioAnalyzer()
    r1 = obj.transcribe(key="same")
    r2 = obj.transcribe(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = AudioAnalyzer()
    obj.transcribe()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = AudioAnalyzer()
    obj.transcribe(x=1)
    obj.detect_speakers(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
