class Dad:
    def football(self):
        print("Dad likes watching football.")



class Mom:
    def cooking(self):
        print("Mom likes cooking.")


class Boy(Dad):
    def boyage(self):
        print("I'm a 20 year old.")


sky=Boy()
sky.football()
sky.boyage()