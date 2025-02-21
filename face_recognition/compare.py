from deepface import DeepFace

def compare_faces(face1, face2):
    """
    Compares two face images using DeepFace's Facenet model.

    Args:
        face1 (str): Path to the first image.
        face2 (str): Path to the second image.

    Returns:
        bool: True if the faces match, False otherwise.
    """
    try:
        result = DeepFace.verify(face1, face2, model_name="Facenet")
        return bool(result.get('verified', False))
    except ValueError:
        return 1
