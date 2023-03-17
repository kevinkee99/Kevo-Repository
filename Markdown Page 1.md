# Page 1: Code Block

> **Description**: This page shows code block that I created for INFOTC-1000 class assignment. This program is called "FizzBuzz" and the purpose of this program is to output nubmer from 1 to 100 with following conditions:
> 1. If the number is divisible by 3, replace it with "Fizz".
> 2. If the number is divisible by 5, replace it with "Buzz".
> 3. If the number is divisble by 3 and 5, replace it with "FizzBuzz".

Below is the fizzbuzz.html file.  

<!DOCTYPE html>  
<html>  
<head>  	
<meta charset="UTF-8">  
<title>Fizz Buzz</title>  	
<script>  	
function fizzbuzz() {  
		var display = document.getElementById('display');  
		var displayHTML = "";  
		for (i = 1; i < 101; i++) {  
				if (i % 3 == 0 && i % 5 == 0) {  
						displayHTML += "<p>" + "FizzBuzz" + "</p>";  
				}  
				else if (i % 3 == 0) {  
						displayHTML += "<p>"+"Fizz"+"</p>";  
				}  								
				else if (i % 5 == 0) {  
						displayHTML += "<p>"+ "Buzz" + "</p>";  
				}  
				else {  
						displayHTML += "<p>" + i + "</p>";  		
  			}  
		}  
		display.innerHTML = displayHTML  
}  
												
</script>  
</head>  	
<body onload="fizzbuzz()">  
<div id="display">  
</div>  
</body>  
</html>  
