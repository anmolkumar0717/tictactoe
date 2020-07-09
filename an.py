<script type="text/javascript">
		var doc=""
		xmlhttp = new XMLHttpRequest();
		xmlhttp.open("GET","assign18.xml",false)
		xmlhttp.onreadystatechange= function(){
			if(xmlhttp.readyState == 4 && xmlhttp.status == 200)
			{
				doc = xmlhttp.responseXML;
				//document.write(doc);
				studentbio=doc.getElementsByTagName('Studentbiodata')[0];
				title=studentbio.childNodes
				//document.write(title.length);
				for(var i=1;i<title.length;i+=2)
				{
					value=title[i].childNodes[0].nodeValue;
					document.write(value+"<br/>");
				}
            }
		}
		xmlhttp.send()

		</script>	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		