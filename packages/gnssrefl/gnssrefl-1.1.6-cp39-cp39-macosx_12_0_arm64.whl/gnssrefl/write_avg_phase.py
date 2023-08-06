def write_avg_phase(station, phase, fr,year,year_end,minvalperday,vxyz):

    """
    parameters
    --------
    station : string

    phase : numpy list of phase values 

    fr : integer
        frequency

    year: integer

    year_end : integer

    minvalperday : integer
        required number of satellite tracks to trust the daily average 

    vxyz is from some other compilation

    returns
    --------
    tv : numpy array with elements
        year, doy, meanph, nvals 

    """
    y1 = vxyz[:, 0]
    d1 = vxyz[:, 1]
    phase = vxyz[:, 2]
    sat = vxyz[:, 3] # this is not used
    az = vxyz[:, 4] # this is not used
    rh = vxyz[:, 5] # this is not used
    amp = vxyz[:, 6]

    tv = np.empty(shape=[0, 4])

    if (fr == 1):
        fileout = xdir + '/Files/' + station + '_phase_L1.txt'
    else:
        fileout = xdir + '/Files/' + station + '_phase.txt'

    print('Daily averaged phases will be written to : ', fileout)
    with open(fileout, 'w') as fout:
        fout.write("% Year DOY Ph Phsig NormA MM DD \n")
        for requested_year in range(year, year_end + 1):
            for doy in range(1, 367):
            # put in amplitude criteria to keep out bad L2P results
                ph1 = phase[(y1 == requested_year) & (d1 == doy) & (phase > -10) & (amp > 0.65)]
                amp1 = amp[(y1 == requested_year) & (d1 == doy) & (phase > -10) & (amp > 0.65)]
                if (len(ph1) > minvalperday):
                    newl = [requested_year, doy, np.mean(ph1), len(ph1)]
                # i think you normalize the individual satellites before this step
                #namp = qp.normAmp(amp1,0.15)
                    tv = np.append(tv, [newl], axis=0)
                    rph1 = np.round(np.mean(ph1), 2)
                    meanA = np.mean(amp1)
                    rph1_std = np.std(ph1)
                    yy, mm, dd, cyyyy, cdoy, YMD = g.ydoy2useful(requested_year, doy)
                    fout.write(f" {requested_year:4.0f} {doy:3.0f} {rph1:6.2f} {rph1_std:6.2f} {meanA:6.3f} {0.0:5.2f}   {mm:2.0f} {dd:2.0f} \n")

        fout.close()
    return tv
