"""Seed script to populate Paint table with Suvinil products."""

from apps.core.api.paint.paint_enums import (
    Environment,
    FinishType,
    PaintLine,
    SurfaceType,
)
from apps.core.database.session import get_session
from apps.core.models.paint import Paint
from apps.core.models.user import User


def create_paint_seeds():
    """Create paint seeds with Suvinil products."""
    with next(get_session()) as session:
        user = session.query(User).first()
        if not user:
            print(
                '⚠️  Nenhum usuário encontrado. Execute o seed de usuários primeiro.'
            )
            return

        user_id = user.id
        print(f'📝 Usando usuário: {user.username} (ID: {user_id})')

        existing_paints = session.query(Paint).count()
        if existing_paints > 0:
            print(
                f'⚠️  Já existem {existing_paints} tintas no banco. Limpando...'
            )
            session.query(Paint).delete()
            session.commit()

        surface_mapping = {
            'Alvenaria': SurfaceType.MASONRY,
            'Madeira': SurfaceType.WOOD,
            'Ferro': SurfaceType.METAL,
            'Metal': SurfaceType.METAL,
            'Concreto': SurfaceType.CONCRETE,
            'Gesso': SurfaceType.PLASTER,
            'Cerâmica': SurfaceType.CERAMIC,
            'Vidro': SurfaceType.GLASS,
            'Plástico': SurfaceType.PLASTIC,
        }

        environment_mapping = {
            'Interno': Environment.INTERNAL,
            'Externo': Environment.EXTERNAL,
            'Interno/Externo': Environment.BOTH,
            'Ambos': Environment.BOTH,
        }

        finish_mapping = {
            'Fosco': FinishType.MATTE,
            'Acetinado': FinishType.SATIN,
            'Semi-brilho': FinishType.SEMI_GLOSS,
            'Brilhante': FinishType.GLOSS,
            'Brilho': FinishType.GLOSS,
            'Metálico': FinishType.METALLIC,
            'Texturizado': FinishType.TEXTURED,
        }

        line_mapping = {
            'Premium': PaintLine.PREMIUM,
            'Standard': PaintLine.STANDARD,
            'Economic': PaintLine.ECONOMIC,
            'Professional': PaintLine.PROFESSIONAL,
            'Specialty': PaintLine.SPECIALTY,
        }

        paint_data = [
            {
                'name': 'Suvinil Toque de Seda',
                'color': 'Branco Neve',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Acetinado',
                'features': 'Lavável, Sem odor, Alta cobertura, Fácil limpeza',
                'paint_line': 'Premium',
            },
            {
                'name': 'Suvinil Fosco Completo',
                'color': 'Cinza Urbano',
                'surface_type': 'Alvenaria',
                'environment': 'Interno/Externo',
                'finish_type': 'Fosco',
                'features': 'Anti-mofo, Alta cobertura, Resistente à umidade',
                'paint_line': 'Premium',
            },
            {
                'name': 'Suvinil Clássica',
                'color': 'Amarelo Canário',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Fosco',
                'features': 'Boa cobertura, Econômica, Rápida secagem',
                'paint_line': 'Standard',
            },
            {
                'name': 'Suvinil Esmalte Sintético',
                'color': 'Vermelho Ferrari',
                'surface_type': 'Madeira',
                'environment': 'Interno/Externo',
                'finish_type': 'Brilhante',
                'features': 'Alta durabilidade, Resistente ao calor, Impermeável',
                'paint_line': 'Premium',
            },
            {
                'name': 'Suvinil Criativa',
                'color': 'Verde Menta',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Fosco',
                'features': 'Sem cheiro, Fácil aplicação, Lavável',
                'paint_line': 'Standard',
            },
            {
                'name': 'Suvinil Fachada Acrílica',
                'color': 'Azul Sereno',
                'surface_type': 'Alvenaria',
                'environment': 'Externo',
                'finish_type': 'Fosco',
                'features': 'Resistente à chuva e sol, Anti-mofo, Lavável',
                'paint_line': 'Premium',
            },
            {
                'name': 'Suvinil Premium Plus',
                'color': 'Branco Gelo',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Acetinado',
                'features': 'Antimicrobiana, Ultra lavável, Cobertura total',
                'paint_line': 'Premium',
            },
            {
                'name': 'Suvinil Metalatex',
                'color': 'Prata Metálico',
                'surface_type': 'Metal',
                'environment': 'Interno/Externo',
                'finish_type': 'Metálico',
                'features': 'Proteção anticorrosiva, Efeito metalizado',
                'paint_line': 'Specialty',
            },
            {
                'name': 'Suvinil Econômica',
                'color': 'Bege Suave',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Fosco',
                'features': 'Boa cobertura, Custo-benefício, Fácil aplicação',
                'paint_line': 'Economic',
            },
            {
                'name': 'Suvinil Casa & Cia',
                'color': 'Rosa Bebê',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Fosco',
                'features': 'Ideal para quarto infantil, Lavável, Sem odor',
                'paint_line': 'Standard',
            },
            {
                'name': 'Suvinil Cor & Proteção',
                'color': 'Azul Oceano',
                'surface_type': 'Alvenaria',
                'environment': 'Externo',
                'finish_type': 'Semi-brilho',
                'features': 'Proteção UV, Resistente à maresia, Durabilidade',
                'paint_line': 'Premium',
            },
            {
                'name': 'Suvinil Madeira & Ferro',
                'color': 'Marrom Chocolate',
                'surface_type': 'Madeira',
                'environment': 'Interno/Externo',
                'finish_type': 'Brilho',
                'features': 'Proteção contra cupins, Resistente à umidade',
                'paint_line': 'Professional',
            },
            {
                'name': 'Suvinil Piso & Azulejo',
                'color': 'Cinza Cimento',
                'surface_type': 'Cerâmica',
                'environment': 'Interno',
                'finish_type': 'Semi-brilho',
                'features': 'Aderência especial, Resistente ao tráfego',
                'paint_line': 'Specialty',
            },
            {
                'name': 'Suvinil Renovação',
                'color': 'Terracota',
                'surface_type': 'Alvenaria',
                'environment': 'Interno/Externo',
                'finish_type': 'Fosco',
                'features': 'Cobertura de manchas, Renovação fácil',
                'paint_line': 'Standard',
            },
            {
                'name': 'Suvinil Concreto Aparente',
                'color': 'Cinza Concreto',
                'surface_type': 'Concreto',
                'environment': 'Interno/Externo',
                'finish_type': 'Fosco',
                'features': 'Impermeabilizante, Proteção contra carbonatação',
                'paint_line': 'Professional',
            },
            {
                'name': 'Suvinil Gesso & Drywall',
                'color': 'Off White',
                'surface_type': 'Gesso',
                'environment': 'Interno',
                'finish_type': 'Fosco',
                'features': 'Aderência especial, Não craquelarenta, Respirável',
                'paint_line': 'Specialty',
            },
            {
                'name': 'Suvinil Vivace',
                'color': 'Laranja Vibrante',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Acetinado',
                'features': 'Cores intensas, Resistência à luz, Lavável',
                'paint_line': 'Premium',
            },
            {
                'name': 'Suvinil Decora',
                'color': 'Roxo Ametista',
                'surface_type': 'Alvenaria',
                'environment': 'Interno',
                'finish_type': 'Fosco',
                'features': 'Efeito aveludado, Fácil retoque, Sem respingos',
                'paint_line': 'Standard',
            },
            {
                'name': 'Suvinil Textura Rústica',
                'color': 'Marfim Rústico',
                'surface_type': 'Alvenaria',
                'environment': 'Interno/Externo',
                'finish_type': 'Texturizado',
                'features': 'Efeito decorativo, Disfarça imperfeições, Durável',
                'paint_line': 'Specialty',
            },
            {
                'name': 'Suvinil Grafiato',
                'color': 'Areia do Deserto',
                'surface_type': 'Alvenaria',
                'environment': 'Externo',
                'finish_type': 'Texturizado',
                'features': 'Textura decorativa, Proteção da parede, Impermeável',
                'paint_line': 'Professional',
            },
        ]

        paints = []
        for data in paint_data:
            try:
                paint = Paint(
                    name=data['name'],
                    color=data['color'],
                    surface_type=surface_mapping[data['surface_type']],
                    environment=environment_mapping[data['environment']],
                    finish_type=finish_mapping[data['finish_type']],
                    features=data['features'],
                    paint_line=line_mapping[data['paint_line']],
                    created_by_user_id=user_id,
                    audit_user_ip='127.0.0.1',
                    audit_user_login=user.username,
                )
                paints.append(paint)
                print(f'✅ Preparando: {paint.name} ({paint.color})')

            except KeyError as e:
                print(f"❌ Erro no mapeamento para {data['name']}: {e}")
                continue

        session.add_all(paints)
        session.commit()

        print(f'\n🎉 {len(paints)} tintas inseridas com sucesso!')
        print('\n📊 Resumo por categoria:')

        from collections import Counter

        lines = Counter([p.paint_line.value for p in paints])
        environments = Counter([p.environment.value for p in paints])
        finishes = Counter([p.finish_type.value for p in paints])
        surfaces = Counter([p.surface_type.value for p in paints])

        print(f'  Linhas: {dict(lines)}')
        print(f'  Ambientes: {dict(environments)}')
        print(f'  Acabamentos: {dict(finishes)}')
        print(f'  Superfícies: {dict(surfaces)}')


if __name__ == '__main__':
    try:
        create_paint_seeds()
    except Exception as e:
        print(f'❌ Erro durante a criação do seed: {e}')
        import traceback

        traceback.print_exc()
