from unittest.mock import patch

from sqlalchemy import select

from apps.core.models.paint import Paint
from tests.factory.paint_factory import PaintFactory


def test_create_paint(session, user):
    """
    Teste de criação de Paint no banco de dados.

    Args:
        session (Session): Instancia de Session do SQLAlchemy provisionada pelo Fixture.
        user (User): Instancia de User provisionada pelo Fixture.
    """

    # GIVEN ------
    # Dada uma Instancia de Paint com os dados abaixo é salva no banco de dados;
    new_paint = PaintFactory.build()
    new_paint.id = None
    new_paint.name = 'Tinta Teste'
    new_paint.created_by_user_id = user.id
    session.add(new_paint)
    session.commit()

    # WHEN ------
    # Quando executa-se uma busca com um filtro que aponta para a tinta anteriormente
    # salva;
    paint = session.scalar(select(Paint).where(Paint.name == 'Tinta Teste'))

    # THEN ------
    # Então uma instancia de Paint é retornada do banco de dados com os mesmos dados que
    # foi salvo anteriormente.
    assert paint.name == 'Tinta Teste'
    assert paint.color == new_paint.color
    assert paint.surface_type == new_paint.surface_type
    assert paint.environment == new_paint.environment
    assert paint.finish_type == new_paint.finish_type
    assert paint.features == new_paint.features
    assert paint.paint_line == new_paint.paint_line
    assert paint.created_by_user_id == user.id
    assert paint.audit_user_ip == new_paint.audit_user_ip
    assert paint.audit_user_login == new_paint.audit_user_login
    assert paint.audit_created_at
    assert paint.audit_updated_on


def test_create_paint_success(client, user, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.post(
            '/paints/',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'name': 'Tinta Premium',
                'color': 'Azul Royal',
                'surface_type': 'wood',
                'environment': 'internal',
                'finish_type': 'satin',
                'features': 'Lavável e resistente',
                'paint_line': 'premium',
                'created_by_user_id': user.id,
            },
        )

    assert response.status_code == 201
    assert response.json()['id']
    assert response.json()['name'] == 'Tinta Premium'
    assert response.json()['color'] == 'Azul Royal'
    assert response.json()['surface_type'] == 'wood'
    assert response.json()['environment'] == 'internal'
    assert response.json()['finish_type'] == 'satin'
    assert response.json()['features'] == 'Lavável e resistente'
    assert response.json()['paint_line'] == 'premium'
    assert response.json()['created_by_user_id'] == user.id
    assert mocked_access_validation.assert_called_once


def test_create_paint_duplicate_success(client, paint, user, token):
    """Test that duplicate paints can be created (no unique constraint)."""
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.post(
            '/paints/',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'name': paint.name,
                'color': paint.color,
                'surface_type': paint.surface_type.value,
                'environment': paint.environment.value,
                'finish_type': paint.finish_type.value,
                'features': paint.features,
                'paint_line': paint.paint_line.value,
                'created_by_user_id': user.id,
            },
        )

    assert response.status_code == 201
    assert response.json()['name'] == paint.name
    assert response.json()['color'] == paint.color
    assert mocked_access_validation.assert_called_once


def test_read_paints(client, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.get(
            '/paints/', headers={'Authorization': f'Bearer {token}'}
        )
    assert response.status_code == 200
    assert 'paints' in response.json()
    assert mocked_access_validation.assert_called_once


def test_get_paint_by_id(client, paint, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.get(
            f'/paints/{paint.id}',
            headers={'Authorization': f'Bearer {token}'},
        )
        assert response.status_code == 200
        assert response.json()['id'] == paint.id
        assert response.json()['name'] == paint.name
        assert response.json()['color'] == paint.color
        assert response.json()['surface_type'] == paint.surface_type.value
        assert response.json()['environment'] == paint.environment.value
        assert response.json()['finish_type'] == paint.finish_type.value
        assert response.json()['features'] == paint.features
        assert response.json()['paint_line'] == paint.paint_line.value
        assert (
            response.json()['created_by_user_id'] == paint.created_by_user_id
        )
        assert mocked_access_validation.assert_called_once


def test_read_paints_with_paints(client, paint, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.get(
            '/paints/', headers={'Authorization': f'Bearer {token}'}
        )

    assert response.status_code == 200
    assert 'paints' in response.json()

    # Verifica se a tinta específica está na lista
    paints_in_response = response.json()['paints']
    paint_found = any(p['id'] == paint.id for p in paints_in_response)
    assert paint_found, f'Paint with id {paint.id} not found in response'

    assert mocked_access_validation.assert_called_once


def test_update_paint_success(client, paint, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.put(
            f'/paints/{paint.id}',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'name': 'Tinta Atualizada',
                'color': 'Verde Esmeralda',
                'surface_type': 'metal',
                'environment': 'external',
                'finish_type': 'gloss',
                'features': 'Anti-ferrugem e resistente ao tempo',
                'paint_line': 'professional',
                'created_by_user_id': paint.created_by_user_id,
            },
        )

    assert response.status_code == 200
    assert response.json()['id'] == paint.id
    assert response.json()['name'] == 'Tinta Atualizada'
    assert response.json()['color'] == 'Verde Esmeralda'
    assert response.json()['surface_type'] == 'metal'
    assert response.json()['environment'] == 'external'
    assert response.json()['finish_type'] == 'gloss'
    assert response.json()['features'] == 'Anti-ferrugem e resistente ao tempo'
    assert response.json()['paint_line'] == 'professional'
    assert response.json()['created_by_user_id'] == paint.created_by_user_id
    assert mocked_access_validation.assert_called_once


def test_update_paint_fail(client, paint):
    response = client.put(
        '/paints/999',
        json={
            'name': 'Tinta Inexistente',
            'color': 'Cor Inexistente',
            'surface_type': 'wood',
            'environment': 'internal',
            'finish_type': 'matte',
            'features': 'Nenhuma',
            'paint_line': 'standard',
            'created_by_user_id': 1,
        },
    )

    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_delete_paint_success(client, paint, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.delete(
            f'/paints/{paint.id}',
            headers={'Authorization': f'Bearer {token}'},
        )

    assert response.status_code == 200
    assert response.json() == {'detail': 'Paint deleted'}
    assert mocked_access_validation.assert_called_once


def test_delete_paint_fail(client):
    response = client.delete('/paints/999')

    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_get_paint_not_found(client, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.get(
            '/paints/999',
            headers={'Authorization': f'Bearer {token}'},
        )
        assert response.status_code == 404
        assert 'not found' in response.json()['detail'].lower()
        assert mocked_access_validation.assert_called_once


def test_update_paint_not_found(client, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.put(
            '/paints/999',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'name': 'Tinta Inexistente',
                'color': 'Cor Inexistente',
                'surface_type': 'wood',
                'environment': 'internal',
                'finish_type': 'matte',
                'features': 'Nenhuma',
                'paint_line': 'standard',
                'created_by_user_id': 1,
            },
        )

    assert response.status_code == 404
    assert 'not found' in response.json()['detail'].lower()
    assert mocked_access_validation.assert_called_once


def test_delete_paint_not_found(client, token):
    with patch(
        'apps.core.api.paint.router.validate_transaction_access'
    ) as mocked_access_validation:
        response = client.delete(
            '/paints/999',
            headers={'Authorization': f'Bearer {token}'},
        )

    assert response.status_code == 404
    assert 'not found' in response.json()['detail'].lower()
    assert mocked_access_validation.assert_called_once
