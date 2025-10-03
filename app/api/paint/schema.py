from app.api.paint.paint_enums import PaintFeature


#TODO: refactor para outro lugar
def get_features_list(self) -> list[PaintFeature]:
    """
    Convert the features string to a list of PaintFeature enums.
    Features are stored as comma-separated values.
    """
    if not self.features:
        return []

    feature_strings = [f.strip() for f in self.features.split(',')]
    features_list = []

    for feature_str in feature_strings:
        try:
            features_list.append(PaintFeature(feature_str))
        except ValueError:
            # Skip invalid feature values
            continue

    return features_list

def set_features_list(self, features: list[PaintFeature]) -> None:
    """
    Set the features from a list of PaintFeature enums.
    Features are stored as comma-separated values.
    """
    if not features:
        self.features = None
    else:
        self.features = ','.join([feature.value for feature in features])
