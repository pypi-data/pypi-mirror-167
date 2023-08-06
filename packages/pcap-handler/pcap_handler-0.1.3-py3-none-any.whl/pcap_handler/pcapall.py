import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # suppress scapy warnings
from scapy.all import *  # Packet manipulation
import pandas as pd  # Pandas - Create and Manipulate DataFrames
import binascii  # Binary to Ascii
from os.path import exists


class pcapHandler:

    """
    :param file: path to pcap file.
    :param verbose: Set verbose status.
    :type verbose: bool

    """

    def __init__(self, file, verbose=False):
        self.verbose = verbose
        if verbose:
            if exists(file):
                try:
                    print("Reading file...")
                    testFile = rdpcap(file)
                    fileType = str(type(testFile))
                    print("Testing file...")
                    if fileType == ("<class 'scapy.plist.PacketList'>"):
                        self.file = testFile
                        print("File is verified!")
                except:
                    raise TypeError("Only .pcap file is allowed")
            else:
                raise FileNotFoundError("File not found!")
        else:
            if exists(file):
                try:
                    testFile = rdpcap(file)
                    fileType = str(type(testFile))
                    if fileType == ("<class 'scapy.plist.PacketList'>"):
                        self.file = testFile
                except:
                    raise TypeError("Only .pcap file is allowed")
            else:
                raise FileNotFoundError("File not found!")

    def to_DF(self, head=False):

        """
        :param head: print first 5 rows after making dataframe.
        :type head: bool
        :return: dataframe from the given file.

        """

        pcap = self.file
        verbose = self.verbose
        if head & verbose:
            # Collect field names from IP/TCP/UDP (These will be columns in DF)
            ip_fields = [field.name for field in IP().fields_desc]
            tcp_fields = [field.name for field in TCP().fields_desc]
            udp_fields = [field.name for field in UDP().fields_desc]

            dataframe_fields = ip_fields + ['time'] + tcp_fields + ['payload', 'payload_raw', 'payload_hex']

            # Create blank DataFrame
            df = pd.DataFrame(columns=dataframe_fields)
            print("Extracting data from pcap file...")
            for packet in pcap[IP]:
                # Field array for each row of DataFrame
                field_values = []
                # Add all IP fields to dataframe
                for field in ip_fields:
                    if field == 'options':
                        # Retrieving number of options defined in IP Header
                        field_values.append(len(packet[IP].fields[field]))
                    else:
                        field_values.append(packet[IP].fields[field])

                field_values.append(packet.time)

                layer_type = type(packet[IP].payload)
                for field in tcp_fields:
                    try:
                        if field == 'options':
                            field_values.append(len(packet[layer_type].fields[field]))
                        else:
                            field_values.append(packet[layer_type].fields[field])
                    except:
                        field_values.append(None)

                # Append payload
                field_values.append(len(packet[layer_type].payload))
                field_values.append(packet[layer_type].payload.original)
                field_values.append(binascii.hexlify(packet[layer_type].payload.original))
                # Add row to DF
                df_append = pd.DataFrame([field_values], columns=dataframe_fields)
                df = pd.concat([df, df_append], axis=0)
            print("Making a dataframe (df)")

            # Reset Index
            df = df.reset_index()
            # Drop old index column
            df = df.drop(columns="index")
            print(df.head())
            return df

        elif head:
            # Collect field names from IP/TCP/UDP (These will be columns in DF)
            ip_fields = [field.name for field in IP().fields_desc]
            tcp_fields = [field.name for field in TCP().fields_desc]
            udp_fields = [field.name for field in UDP().fields_desc]

            dataframe_fields = ip_fields + ['time'] + tcp_fields + ['payload', 'payload_raw', 'payload_hex']

            # Create blank DataFrame
            df = pd.DataFrame(columns=dataframe_fields)
            for packet in pcap[IP]:
                # Field array for each row of DataFrame
                field_values = []
                # Add all IP fields to dataframe
                for field in ip_fields:
                    if field == 'options':
                        # Retrieving number of options defined in IP Header
                        field_values.append(len(packet[IP].fields[field]))
                    else:
                        field_values.append(packet[IP].fields[field])

                field_values.append(packet.time)

                layer_type = type(packet[IP].payload)
                for field in tcp_fields:
                    try:
                        if field == 'options':
                            field_values.append(len(packet[layer_type].fields[field]))
                        else:
                            field_values.append(packet[layer_type].fields[field])
                    except:
                        field_values.append(None)

                # Append payload
                field_values.append(len(packet[layer_type].payload))
                field_values.append(packet[layer_type].payload.original)
                field_values.append(binascii.hexlify(packet[layer_type].payload.original))
                # Add row to DF
                df_append = pd.DataFrame([field_values], columns=dataframe_fields)
                df = pd.concat([df, df_append], axis=0)

            # Reset Index
            df = df.reset_index()
            # Drop old index column
            df = df.drop(columns="index")
            print(df.head())
            return df

        elif verbose:
            # Collect field names from IP/TCP/UDP (These will be columns in DF)
            ip_fields = [field.name for field in IP().fields_desc]
            tcp_fields = [field.name for field in TCP().fields_desc]
            udp_fields = [field.name for field in UDP().fields_desc]

            dataframe_fields = ip_fields + ['time'] + tcp_fields + ['payload', 'payload_raw', 'payload_hex']

            # Create blank DataFrame
            df = pd.DataFrame(columns=dataframe_fields)
            print("Extracting data from pcap file...")
            for packet in pcap[IP]:
                # Field array for each row of DataFrame
                field_values = []
                # Add all IP fields to dataframe
                for field in ip_fields:
                    if field == 'options':
                        # Retrieving number of options defined in IP Header
                        field_values.append(len(packet[IP].fields[field]))
                    else:
                        field_values.append(packet[IP].fields[field])

                field_values.append(packet.time)

                layer_type = type(packet[IP].payload)
                for field in tcp_fields:
                    try:
                        if field == 'options':
                            field_values.append(len(packet[layer_type].fields[field]))
                        else:
                            field_values.append(packet[layer_type].fields[field])
                    except:
                        field_values.append(None)
                # Append payload
                field_values.append(len(packet[layer_type].payload))
                field_values.append(packet[layer_type].payload.original)
                field_values.append(binascii.hexlify(packet[layer_type].payload.original))
                # Add row to DF
                df_append = pd.DataFrame([field_values], columns=dataframe_fields)
                df = pd.concat([df, df_append], axis=0)
            print("Making a dataframe (df)")

            # Reset Index
            df = df.reset_index()
            # Drop old index column
            df = df.drop(columns="index")
            return df
        else:
            # Collect field names from IP/TCP/UDP (These will be columns in DF)
            ip_fields = [field.name for field in IP().fields_desc]
            tcp_fields = [field.name for field in TCP().fields_desc]
            udp_fields = [field.name for field in UDP().fields_desc]

            dataframe_fields = ip_fields + ['time'] + tcp_fields + ['payload', 'payload_raw', 'payload_hex']

            # Create blank DataFrame
            df = pd.DataFrame(columns=dataframe_fields)
            for packet in pcap[IP]:
                # Field array for each row of DataFrame
                field_values = []
                # Add all IP fields to dataframe
                for field in ip_fields:
                    if field == 'options':
                        # Retrieving number of options defined in IP Header
                        field_values.append(len(packet[IP].fields[field]))
                    else:
                        field_values.append(packet[IP].fields[field])

                field_values.append(packet.time)

                layer_type = type(packet[IP].payload)
                for field in tcp_fields:
                    try:
                        if field == 'options':
                            field_values.append(len(packet[layer_type].fields[field]))
                        else:
                            field_values.append(packet[layer_type].fields[field])
                    except:
                        field_values.append(None)

                # Append payload
                field_values.append(len(packet[layer_type].payload))
                field_values.append(packet[layer_type].payload.original)
                field_values.append(binascii.hexlify(packet[layer_type].payload.original))
                # Add row to DF
                df_append = pd.DataFrame([field_values], columns=dataframe_fields)
                df = pd.concat([df, df_append], axis=0)

            # Reset Index
            df = df.reset_index()
            # Drop old index column
            df = df.drop(columns="index")
            return df
        # print("dataframe is built and can be accessed by making an object of .to_df()")


class dfHandler:
    """
    :param dataFrame: pandas DataFrame object.
    :param verbose: Set verbose status.
    :type verbose: bool

    """

    def __init__(self, dataFrame, verbose=False):
        self.verbose = verbose
        if verbose:
            print("Checking DataFrame...")
            if isinstance(dataFrame, pd.DataFrame):
                self.dataFrame = dataFrame
                print("DataFrame Verified!")
            else:
                raise TypeError("only pandas Dataframe is allowed")

        else:
            if isinstance(dataFrame, pd.DataFrame):
                self.dataFrame = dataFrame
            else:
                raise TypeError("only pandas Dataframe is allowed")
    def to_CSV(self, outputPath):
        """
        :param outputPath: path to save csv file.
        """
        verbose = self.verbose
        dataFrame = self.dataFrame
        if verbose:
            print("Converting to CSV...")
            dataFrame.to_csv(outputPath, encoding='utf-8')
            print(f"Done! File saved at {outputPath}")
