import hashlib
class GetMD5():
    @staticmethod
    def getMD5(str):
      """get the digest of str"""
      m = hashlib.md5()
      m.update(str)
      return m.hexdigest().decode("ascii").encode("utf-8")

