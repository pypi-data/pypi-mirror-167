def encode_callsign(callsign, ssid):
    """
    Encodes a given callsign.

    :param callsign: is the callsign to encode (ASCII string).
    :param ssid: is the SSID to encode with the callsign (integer).

    :return The encoded callsign as a list of integers (bytes).
    """
    if (len(callsign) > 7) or (ssid >= 100):
        return list()

    # Convert to uppercase
    callsign = callsign.upper()

    # Convert to list of characters
    callsign = list(callsign)
 
    enc_callsign = list()

    for i in callsign:
        enc_callsign.append(ord(i))

    for i in range(7 - len(callsign)):
        enc_callsign.append(ord(' '))

    enc_callsign.append(ssid)

    return enc_callsign


def decode_callsign(enc_callsign):
    """
    Decodes a given encoded callsign.

    :param enc_callsign: the encoded callsign to decode.

    :return The decoded callsign as an string.
    """
    callsign = str()

    for i in range(7):
        if enc_callsign[i] != ord(' '):
            callsign = callsign + chr(enc_callsign[i])

    return callsign, enc_callsign[-1]


msg = encode_callsign("PU5GMA", 1)

print(msg)
print(decode_callsign(msg))
