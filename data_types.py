class Purchase:
    def __init__(
            self, idvariable, fecha, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11,
            var12, var13, var14, var15, var16, var17, var18, var19, var20, status, iddispositivo):
        self.idvariable = idvariable
        self.fecha = fecha
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.var5 = var5
        self.var6 = var6
        self.var7 = var7
        self.var8 = var8
        self.var9 = var9
        self.var10 = var10
        self.var11 = var11
        self.var12 = var12
        self.var13 = var13
        self.var14 = var14
        self.var15 = var15
        self.var16 = var16
        self.var17 = var17
        self.var18 = var18
        self.var19 = var19
        self.var20 = var20
        self.status = status
        self.iddispositivo = iddispositivo

    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            int(lookup['idvariable']),
            lookup['fecha'],
            float(lookup['var1']),
            float(lookup['var2']),
            float(lookup['var3']),
            float(lookup['var4']),
            float(lookup['var5']),
            float(lookup['var6']),
            float(lookup['var7']),
            float(lookup['var8']),
            float(lookup['var9']),
            float(lookup['var10']),
            float(lookup['var11']),
            float(lookup['var12']),
            float(lookup['var13']),
            float(lookup['var14']),
            float(lookup['var15']),
            float(lookup['var16']),
            float(lookup['var17']),
            float(lookup['var18']),
            float(lookup['var19']),
            float(lookup['var20']),
            int(lookup['status']),
            int(lookup['iddispositivo']))
