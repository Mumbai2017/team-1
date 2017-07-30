<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body bgcolor="lightblue">
  <h1 style="color:blue"><i>D12C Marksheet</i></h1>
    <table border="2" width="80%" height="50%">
      <tr bgcolor="grey">
        <th style="text-align:center;color:white">Name</th>
        <th style="text-align:center;color:white">OS</th>
		<th style="text-align:center;color:white">SOOAD</th>
		<th style="text-align:center;color:white">WT</th>
		<th style="text-align:center;color:white">MP</th>
		<th style="text-align:center;color:white">Total</th>
      </tr>
      <xsl:for-each select="catalog/info">
      <tr bgcolor="white">
        <td style="text-align:center"><xsl:value-of select="name"/></td>
        <td style="text-align:center"><xsl:value-of select="os"/></td>
		<td style="text-align:center"><xsl:value-of select="sooad"/></td>
		<td style="text-align:center"><xsl:value-of select="wt"/></td>
		<td style="text-align:center"><xsl:value-of select="mp"/></td>
		<td style="text-align:center"><b><xsl:value-of select="total"/></b></td>
      </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>

