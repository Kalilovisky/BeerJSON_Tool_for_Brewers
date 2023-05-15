class HopStrain:
    def __init__(self, name, origin, alpha, purpose, beta, profile, cohumulone):
        self.name = name
        self.origin = origin
        self.alpha = alpha
        self.purpose = purpose
        self.beta = beta
        self.profile = profile
        self.cohumulone = cohumulone

    def to_json(self):
        return {
            "name": self.name,
            "origin": self.origin,
            "alpha": self.alpha,
            "purpose": self.purpose,
            "beta": self.beta,
            "profile": self.profile,
            "cohumulone": self.cohumulone
        }