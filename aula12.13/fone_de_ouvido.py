class FoneDeOuvido:
    volume = 0
    def get_volume(self):
        return self.volume
    
    def set_volume(self, novo_volume):
        self.volume = novo_volume

    volume = property(get_volume, set_volume)

fone = FoneDeOuvido()

fone.set_volume = 200
fone.get_volume = 10
print(fone.get_volume)
print(fone.set_volume)