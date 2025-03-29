from uuid import UUID


class CustomerAddress:
    """A Domain Entity representing a Customer Address in the system."""

    def __init__(
            self,
            id: UUID, 
            number: str, 
            city: str, 
            state: str, 
            zip_code: str, 
            country: str, 
            complement: str, 
            address: str
        ):
        id = id
        self.number = number
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.complement = complement
        self.address = address


    def __repr__(self):
        return f"CustomerAddress(number={self.number}, city={self.city}, state={self.state}, zip_code={self.zip_code}, country={self.country}, complement={self.complement}, address={self.address})"