def safe_float(object):
    'safe version of float()'
    try:
        result = float(object)
    except (ValueError,TypeError), e:
        result = str(e)
    return result

def main():
    'handles all the processing'
    log = open('cardlog','w')
    try:
        ccfile = open('carddata')
    except IOError,e:
        log.write('No txns this month\n')
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.0
    log.write('account log: \n')
    for txn in txns:
        result = safe_float(txn)
        if isinstance(result,float):
            total += result
            log.write('data...processed\n')
        else:
            log.write('ignored: %s'% result)

    print '$%.2f (new balance)'% total
    log.close()

if __name__=='__main__':
    main()
