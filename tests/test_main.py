"""
Tests for EinSof AGI API
"""

import pytest
from einsof_agi_api import EinSofAGIAPI


@pytest.fixture
def system():
    """Create system instance for tests"""
    return EinSofAGIAPI()


def test_initialization(system):
    """Test system initialization"""
    assert system.version == "1.0.0"
    assert system.status == "MVP"


def test_process(system):
    """Test process function"""
    result = system.process({"test": "input"})
    
    assert result["status"] == "success"
    assert result["project"] == "EinSof AGI API"
    assert result["version"] == "1.0.0"


def test_info(system):
    """Test get_info function"""
    info = system.get_info()
    
    assert info["name"] == "EinSof AGI API"
    assert info["version"] == "1.0.0"
    assert info["type"] == "api"


@pytest.mark.asyncio
async def test_async_process(system):
    """Test async process"""
    result = await system.process_async({"test": "async"})
    assert result["status"] == "success"
