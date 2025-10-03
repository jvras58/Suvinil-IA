"""Enumerations for Paint model attributes."""
from enum import Enum


class SurfaceType(Enum):
    """Types of surfaces that paint can be applied to."""

    WOOD = "wood"  # Madeira
    METAL = "metal"  # Metal
    MASONRY = "masonry"  # Alvenaria
    CONCRETE = "concrete"  # Concreto
    PLASTER = "plaster"  # Reboco/Gesso
    CERAMIC = "ceramic"  # Cerâmica
    GLASS = "glass"  # Vidro
    PLASTIC = "plastic"  # Plástico


class Environment(Enum):
    """Environment where paint is suitable for use."""

    INTERNAL = "internal"  # Interno
    EXTERNAL = "external"  # Externo
    BOTH = "both"  # Ambos


class FinishType(Enum):
    """Types of paint finish."""

    MATTE = "matte"  # Fosco
    SATIN = "satin"  # Acetinado
    SEMI_GLOSS = "semi_gloss"  # Semi-brilho
    GLOSS = "gloss"  # Brilho
    METALLIC = "metallic"  # Metálico
    TEXTURED = "textured"  # Texturizado


class PaintFeature(Enum):
    """Special features of paint."""

    WASHABLE = "washable"  # Lavável
    ANTI_MOLD = "anti_mold"  # Anti-mofo
    ODORLESS = "odorless"  # Sem odor
    QUICK_DRY = "quick_dry"  # Secagem rápida
    HIGH_COVERAGE = "high_coverage"  # Alto rendimento
    UV_RESISTANT = "uv_resistant"  # Resistente ao UV
    ANTIBACTERIAL = "antibacterial"  # Antibacteriana
    THERMAL_INSULATION = "thermal_insulation"  # Isolamento térmico


class PaintLine(Enum):
    """Paint product lines."""

    PREMIUM = "premium"  # Premium
    STANDARD = "standard"  # Standard
    ECONOMIC = "economic"  # Econômica
    PROFESSIONAL = "professional"  # Profissional
    SPECIALTY = "specialty"  # Especialidade
