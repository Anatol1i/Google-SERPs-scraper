javascript:(function(){
    var output = '<html><head><title>Extraction tool URL from SERP Google </title><style type="text/css">body,table{font-family:Tahoma,Verdana,Segoe,sans-serif;font-size:11px;color:#000}h1,h2,th{color:#000}th{text-align:left}h2{font-size:14px;margin-bottom:3px}</style></head><body>';
    output += '<h1>Extraction tool URL from SERP Google</h1><br>';
    
    var pageAnchors = document.getElementsByTagName('a');
    var linkcount = 0;
    var linkLocation = '';
    output += '<table><th>ID</th><th>URL</th>';

    for (var i = 0; i < pageAnchors.length; i++) {
        var anchorLink = pageAnchors[i].href;
        if (anchorLink != '' && anchorLink.match(/^((?!google\.|cache|blogger.com|\.yahoo\.|youtube\.com\/\?gl=|youtube\.com\/results|javascript:|api\.technorati\.com|botw\.org\/search|del\.icio\.us\/url\/check|digg\.com\/search|search\.twitter\.com\/search|search\.yahoo\.com\/search|siteanalytics\.compete\.com|tools\.seobook\.com\/general\/keyword\/suggestions|web\.archive\.org\/web\/|whois\.domaintools\.com|www\.alexa\.com\/data\/details\/main|www\.bloglines\.com\/search|www\.majesticseo\.com\/search\.php|www\.semrush\.com\/info\/|www\.semrush\.com\/search\.php|www\.stumbleupon\.com\/url|wikipedia.org\/wiki\/Special:Search).)*$/i)) {
            linkLocation += anchorLink + '\n';
           linkcount++;
            output += '<tr>';
            output += '<td>' + linkcount + '</td>';
            output += '<td>' + anchorLink + '</td>';
            output += '</tr>\n';
        }
    }

    output += '</table>';
output += '<a id="DownloadLink" style="display:none;"></a>';
  output += '</body></html>';

    var newWindow = window.open();
  newWindow.document.write(output);
  newWindow.document.close();

  var blob = new Blob([linkLocation], { type: 'text/plain' }),
      downloadLink = newWindow.document.getElementById('DownloadLink');

  downloadLink.href = URL.createObjectURL(blob);
  downloadLink.download = 'uploaded_urls.txt';
  downloadLink.style.display = 'block';
  downloadLink.textContent = 'Download URLs as Text File';
  newWindow.document.body.appendChild(downloadLink);
})();
