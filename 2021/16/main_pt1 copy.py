data = open("input_test.txt", 'r').readlines()
hexData = [int(x, 16) for x in data[0]]
binaryData = [x for x in "".join(["{0:04b}".format(h) for h in hexData])]

class Packet:
    def __init__(self, version, typeID):
          self.version = version
          self.typeID = typeID
      

class Literal(Packet):  
    def __init__(self, version, typeID, literal):
          self.version = version
          self.typeID = typeID
          self.literal = literal
    def SumVersions(self):
          return self.version

class Operator(Packet): 
    def __init__(self, version, typeID, packets):
          self.version = version
          self.typeID = typeID
          self.packets = packets

    def SumVersions(self):
          vsum = self.version
          vsum += sum([packet.SumVersions() for packet in self.packets])
          return vsum
      

def ReadBinary(data, length):
      binary = data[0:length]
      del data[0:length]
      return "".join(binary)
      

def ReadBinaryAsInt(data, length):
      return int("".join(ReadBinary(data, length)), 2)

def ReadLiteral(data):
      literalString = ""
      while ReadBinaryAsInt(data, 1) == 1:
            literalString += ReadBinary(data, 4)
      literalString += ReadBinary(data, 4)
      return int(literalString, 2)
            
def ReadOperator(data):
      packets = []
      lengthTypeID = ReadBinaryAsInt(data, 1)

      if lengthTypeID == 0:
            subPacketLength = ReadBinaryAsInt(data, 15)
            print("lengthTypeID: " + str(lengthTypeID) + "; subPacketLength: " + str(subPacketLength))

            subpacketsData = data[0:subPacketLength]
            del data[0:subPacketLength]
            while len(subpacketsData) > 0:
                  packets.extend(ReadPacket(subpacketsData))
      else:           
            subpacketCount = ReadBinaryAsInt(data, 11)     
            print("lengthTypeID: " + str(lengthTypeID) + "; subpacketCount: " + str(subpacketCount))

            for i in range(0, subpacketCount):
                  packets.extend(ReadPacket(data))
      return packets
      

def ReadPacket(data):
      packets = []
      version = ReadBinaryAsInt(data, 3)
      typeID = ReadBinaryAsInt(data, 3)

      print("version: " + str(version) + "; typeID: " + str(typeID))
      
      if typeID == 4:
            literal = ReadLiteral(data)
            print("literal: " + str(literal))
            packets.append(Literal(version, typeID, literal))
      else:
            packets.append(Operator(version, typeID, ReadOperator(data)))

      return packets

packets = ReadPacket(binaryData)
vsum = sum([packet.SumVersions() for packet in packets])
print(vsum)
