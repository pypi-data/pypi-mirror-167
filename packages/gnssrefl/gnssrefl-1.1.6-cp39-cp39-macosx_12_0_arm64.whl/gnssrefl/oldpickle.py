       if not foundit:
            pname =  'gnssrefl/gpt_1wA.pickle'
            print('2nd attempt: subdirectory gnssrefl of current working directory:', pname)
            if os.path.isfile(pname):
                f = open(pname, 'rb')
                [All_pgrid, All_Tgrid, All_Qgrid, All_dTgrid, All_U, All_Hs, All_ahgrid, All_awgrid, All_lagrid, All_Tmgrid] = pickle.load(f)
                f.close()
                foundit = True
        if not foundit:
            pname = try3
            print('3rd attempt try here: ',pname)
            if os.path.isfile(pname):
                f = open(pname, 'rb')
                [All_pgrid, All_Tgrid, All_Qgrid, All_dTgrid, All_U, All_Hs, All_ahgrid, All_awgrid, All_lagrid, All_Tmgrid] = pickle.load(f)
                f.close()
                foundit = True
        if not foundit:
            print('fourth attempt - download from github')
            try:
                pfile = 'gpt_1wA.pickle'
                url= 'https://github.com/kristinemlarson/gnssrefl/raw/master/gnssrefl/' + pfile
                wget.download(url,pfile)
                subprocess.call(['mv','-f',pfile, xdir + '/input/' ])
                foundit = True
            except:
                print('Failed again.')
        if not foundit:
            print('fifth attempt - this is getting ridiculous')
            pname = xdir + '/input/' + 'gpt_1wA.pickle'
            print(pname)
            try:
                pfile = 'gpt_1wA.pickle'
                url= 'https://morefunwithgps.com/public_html/' + pfile
                wget.download(url,pname)
                #subprocess.call(['mv','-f',pfile, xdir + '/input/' ])
                foundit = True
            except:
                print('Failed again.')
