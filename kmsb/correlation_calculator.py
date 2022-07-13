import numpy as np

def correlations(intensities):
    
    imf = np.float32(intensities)
    height = np.shape(imf)[0]
    width = np.shape(imf)[1]
    
    x1h = intensities
    x2h = np.zeros([height, width])
    for i in range(0, height):
        for j in range(0, width-1):
            x2h[i][j] = x1h[i][j+1]
        x2h[i][width-1] = x1h[i][width-1]

    total_N = np.size(x1h)
    mean_x1h = x1h.sum()/total_N
    mean_x2h = x2h.sum()/total_N

    aa1 = (x1h - mean_x1h)**2
    bb1 = aa1.sum()
    std_dev1 = np.sqrt(bb1/total_N)

    aa2 = (x2h - mean_x2h)**2
    bb2 = aa2.sum()
    std_dev2 = np.sqrt(bb2/total_N)

    cc = (x1h - mean_x1h)*(x2h - mean_x2h)
    hcov = cc.sum()/total_N

    hcorr = hcov/(std_dev1 * std_dev2)
#     print('hcorr', hcorr)

    # Vertical correlation
    x1v = intensities
    x2v = np.zeros([height, width])
    for i in range(0, height-1):
        for j in range(0, width):
            x2v[i][j] = x1v[i+1][j]
            x2v[height-1][j] = x1v[height-1][j]

    total_N = np.size(x1v)
    mean_x1v = x1v.sum()/total_N
    mean_x2v = x2v.sum()/total_N

    aa1 = (x1v - mean_x1v)**2
    bb1 = aa1.sum()
    std_dev1 = np.sqrt(bb1/total_N)

    aa2 = (x2v - mean_x2v)**2
    bb2 = aa2.sum()
    std_dev2 = np.sqrt(bb2/total_N)

    cc = (x1v - mean_x1v)*(x2v - mean_x2v)
    vcov = cc.sum()/total_N

    vcorr = vcov/(std_dev1 * std_dev2)
#     print('vcorr',vcorr)

    # Diagonal correlation
    x1d = intensities
    x2d = np.zeros([height, width])
    for i in range(0, height-1):
        for j in range(0, width-1):
            x2d[i][j] = x1d[i+1][j+1]
            x2d[height-1][j] = x1d[height-1][j]
        x2d[i][width-1] = x1d[i][width-1]
    x2d[height-1][width-1] = x1d[height-1][width-1]

    total_N = np.size(x1d)
    mean_x1d = x1d.sum()/total_N
    mean_x2d = x2d.sum()/total_N

    aa1 = (x1d - mean_x1d)**2
    bb1 = aa1.sum()
    std_dev1 = np.sqrt(bb1/total_N)

    aa2 = (x2d - mean_x2d)**2
    bb2 = aa2.sum()
    std_dev2 = np.sqrt(bb2/total_N)

    cc = (x1d - mean_x1d)*(x2d - mean_x2d)
    dcov = cc.sum()/total_N

    dcorr = dcov/(std_dev1 * std_dev2)
#     print('dcorr',dcorr)
    
    return hcorr, vcorr, dcorr
