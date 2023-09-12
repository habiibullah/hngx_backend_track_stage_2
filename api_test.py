import requests

# Define the base URL of your API
base_url = 'http://localhost:5000/api'

def test_create_person():
    data = {'name': 'Mark Essien'}
    response = requests.post(f'{base_url}', json=data)
    assert response.status_code == 201
    print("Create Person: Passed")

def test_read_person():
    response = requests.get(f'{base_url}/Mark Essien')
    assert response.status_code == 200
    result = response.json()
    assert result['name'] == 'Mark Essien'
    print("Read Person: Passed")

def test_update_person():
    updated_data = {'name': 'Updated Mark Essien'}
    response = requests.put(f'{base_url}/Mark Essien', json=updated_data)
    assert response.status_code == 200
    result = response.json()
    assert result['message'] == 'Person updated successfully'
    print("Update Person: Passed")

def test_delete_person():
    response = requests.delete(f'{base_url}/Updated Mark Essien')
    assert response.status_code == 200
    result = response.json()
    assert result['message'] == 'Person deleted successfully'
    print("Delete Person: Passed")

if __name__ == '__main__':
    try:
        test_create_person()
        test_read_person()
        test_update_person()
        test_delete_person()
    except AssertionError as e:
        print(f"Test failed: {str(e)}")
