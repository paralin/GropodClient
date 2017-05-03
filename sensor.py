import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 1
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE))

def readPH():
	return (3.5 * mcp.read_adc(1))/310.3 + 2

def readEC():
	return 3.5 * mcp.read_adc(0) - 244
