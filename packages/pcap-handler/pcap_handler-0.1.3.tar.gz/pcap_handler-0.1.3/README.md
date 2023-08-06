# import library as:
	from pcap_handler import *
				or
	from pcap_handler import pcapHandler
				or
	from pcap_handler import dfHandler

# Make an object of library
## To convert pcap to pandas DataFrame:
	pcap2df = pcapHandler(file="path to pcap file", verbose=True)
	df = pcap2df.to_DF(head=True)

## To conver DataFrame to CSV:
	df2csv = dfHandler(dataFrame=df, verbose=True)
	df2csv.to_CSV(outputPath="path to save csv")

### Descriptive README soon...