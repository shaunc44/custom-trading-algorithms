var colorChange = document.querySelectorAll(".colorChange");

var updateColor = function(){
	// console.log("change color")
	this.style.setProperty("color", "black");
}

colorChange.forEach(input => input.addEventListener("change", updateColor));