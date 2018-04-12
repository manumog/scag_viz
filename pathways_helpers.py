def arb_emissions(file, columns = 'sectors', sector = 'all', cases = 'Reference'):
    sector_emissions = pd.read_csv(file)
    if columns == 'sectors':
        columns = ['ARB_Sectors1','Active_Cases']
    else:
        columns = ['Active_Cases', 'ARB_Sectors1']

    arb = pd.pivot_table(sector_emissions.query('Geography_SCAG in "SCAG"'),
                         index = 'Output_Year', columns = columns,
                         values = 'Value', aggfunc = np.sum)

    if sector == 'all':
        arb = arb
    else:
        arb = arb[sector]

    return arb

def save_fig(filename):
    plt.savefig('S:\E3 Projects\SCAG Pathways\Report\\' + filename + '.png', dpi = 300, transparent = True)
