# Goal: Create a reusable TCP socket

import logging
import socket

log = logging.getLogger(__name__)

class TcpSocket():
    """
    A class used to represent a TCP socket for remote communication
    to a SpikeSafe

    ...

    Attributes
    ----------
    tcp_socket : TcpSocket
        TCP/IP socket for remote communication to a SpikeSafe

    Methods
    -------
    open_socket(self, ip_address, port_number)
        Opens a TCP/IP socket for remote communication to a SpikeSafe
    close_socket(self)
        Closes TCP/IP socket used for remote communication to a SpikeSafe
    send_scpi_command(self, scpi_command)
        Sends a SCPI command via TCP/IP socket to a SpikeSafe
    read_data(self)
        Reads data reply via TCP/IP socket from a SpikeSafe
    """

    tcp_socket = None

    # create a connection via socket
    def open_socket(self, ip_address, port_number):
        """Opens a TCP/IP socket for remote communication to a SpikeSafe

        Parameters
        ----------
        ip_address : str
            IP address of the SpikeSafe (10.0.0.220 to 10.0.0.0.251)
        port_number : int
            Port number of the SpikeSafe (8282 by default)

        Raises
        ------
        Exception
            On any error
        """
        try:
            # create socket with 2 second timeout and connect to SpikeSafe
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
            self.tcp_socket.settimeout(2)                                                
            self.tcp_socket.connect((ip_address, port_number))                           
        except Exception as err:
            # print any error to terminal and raise error to function caller
            log.error('Error connecting to socket at {}: {}'.format(ip_address, err))   
            raise                                                                   

    # close a connection via socket
    def close_socket(self):
        """Closes TCP/IP socket used for remote communication to a SpikeSafe

        Raises
        ------
        Exception
            On any error
        """
        try:
            # disconnect from socket
            self.tcp_socket.close()  
        except Exception as err:
            # print any error to terminal and raise error to function caller
            log.error('Error disconnecting from socket: {}'.format(err))    
            raise                                                       
        
    # send a SCPI command via socket
    def send_scpi_command(self, scpi_command):
        """Sends a SCPI command via TCP/IP socket to a SpikeSafe

        Parameters
        ----------
        scpi_command : str
            SCPI command to send to SpikeSafe

        Raises
        ------
        Exception
            On any error
        """
        try:
            # add \n termination to SCPI command
            # encode SCPI command to type byte, which is the format required by the socket
            # send byte to socket
            scpi_command_str = scpi_command + '\n'                          
            scpi_command_byte = scpi_command_str.encode()                   
            self.tcp_socket.send(scpi_command_byte)                              
        except Exception as err:
            # print any error to terminal and raise error to function caller
            log.error('Error sending SCPI command to socket: {}'.format(err))   
            raise                                                           

    # read data via socket
    def read_data(self):
        """Reads data reply via TCP/IP socket from a SpikeSafe

        Returns
        -------
        str
            Data response from SpikeSafe

        Raises
        ------
        Exception
            On any error
        """
        try:
            # read data from socket, which is automatically converted from type byte to type string
            # return data to function calle
            data_str = self.tcp_socket.recv(2048) 
            return data_str                                                    
        except Exception as err:
            # print any error to terminal and raise error to function caller
            log.error('Error reading data from socket: {}'.format(err))         
            raise

    # read data via socket
    def read_data_until_end(self):
        """Reads data reply via TCP/IP socket from a SpikeSafe

        Returns
        -------
        str
            Data response from SpikeSafe

        Raises
        ------
        Exception
            On any error
        """
        try:
            # read data from socket, which is automatically converted from type byte to type string
            # return data to function called
            data_str = ''
            last_data_str = data_str

            while True:
                last_data_str = data_str
                data_str += self.tcp_socket.recv(2048)
                if data_str.endswith("\n") or (last_data_str == data_str):
                    break

            return data_str                                                 
        except Exception as err:
            # print any error to terminal and raise error to function caller
            log.error('Error reading data from socket: {}'.format(err))         
            raise                                                         