<!DOCTYPE html>
<html>
  <head>
    <title>script_muldemo.html</title>
  
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="this is my page">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    
    <!--<link rel="stylesheet" type="text/css" href="./styles.css">-->
  <script language = "javascript">
    document.write("<table border = \"1\">");
    for(i=1;i<=9;i++)
    {
      document.write("<tr>")
      for(j=1;j<=9;j++)
      {
        if(j<=i)
        {
          document.write("<td>"+i+"*"+j+"="+i*j+"</td>");
        }
        else
        {
        document.write("<td>&nbsp;</td>")
        }
      }
      document.write("<tr>")
    }
      document.write("</table>")
  </script>
  </head>
  
  <body>
    
  </body>
</html>
