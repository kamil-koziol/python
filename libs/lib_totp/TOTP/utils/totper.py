from .user import User
import pyotp

class TOTPer(pyotp.TOTP):

    def __init__(self, user: User):
        super().__init__(user.secretKey)
        self.user: User = user

    def getCode(self) -> int:
        return int(self.now())
    
    def getURL(self) -> str:
        uri = self.provisioning_uri(name=self.user.name, issuer_name="TOTP Python")
        return uri
    
    def checkCode(self, code: int) -> bool:
        return code == self.getCode()

