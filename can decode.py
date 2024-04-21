def BLF_reader(blffile_address, dbc_file, output_file, channel, ID_name, signal):
    import can
    import cantools
    from datetime import datetime
    dbc = cantools.db.load_file(dbc_file)
    blf_data = can.BLFReader(blffile_address)

    with open(output_file, 'w') as file:
        for msg in blf_data:
            if msg.channel == channel and msg.arbitration_id == ID_name:
                signal_value = dbc.decode_message(ID_name, msg.data)
                output = f"{datetime.fromtimestamp(msg.timestamp)}, {signal_value[signal]}"
                file.write(output)


def ASC_reader(ascfile_address, dbc_file, output_file, channel, ID_name, signal):
    import can
    import cantools
    from datetime import datetime
    dbc = cantools.db.load_file(dbc_file)
    asc_data = can.ASCReader(ascfile_address)

    with open(output_file, 'w') as file:
        for msg in asc_data:
            if msg.channel == channel and msg.arbitration_id == ID_name:
                signal_value = dbc.decode_message(ID_name, msg.data)
                output = f"{msg.timestamp}, {signal_value[signal]}"
                file.write(output)

if __name__ == '__main__':
    BLF_reader('aa.blf', 'xxx.dbc', '11.txt', 1, '0xD', 'speed')
    ASC_reader('aa.asc', 'xxx.dbc', '11.txt', 1, '0xD', 'speed')