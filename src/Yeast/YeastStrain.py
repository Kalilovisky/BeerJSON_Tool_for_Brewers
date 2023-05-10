class YeastStrain:
    def __init__(self, name, beer_type, form, laboratory, product_id, min_temp, max_temp, attenuation, flocculation):
        self.name = name
        self.beer_type = beer_type
        self.form = form
        self.laboratory = laboratory
        self.product_id = product_id
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.attenuation = attenuation
        self.flocculation = flocculation

    def to_json(self):
        return {
            "name": self.name,
            "type": self.beer_type,
            "form": self.form,
            "laboratory": self.laboratory,
            "product_id": self.product_id,
            "min_temperature": self.min_temp,
            "max_temperature": self.max_temp,
            "attenuation": self.attenuation,
            "flocculation": self.flocculation
        }