<script>
        // Adult, Child and Infant values on start point, creating options for tag select
            var options = "";
            for(var i = 1; i<10; i++ ) {
                options += "<option val="+i+">"+i+"</option>";
                document.getElementById('adult').innerHTML = options
                };

            var options = "";
            for(var i = 0; i<9; i++ ) {
                options += "<option val="+i+">"+i+"</option>";
                document.getElementById('child').innerHTML = options
                };

            var options = "";
            for(var i = 0; i<2; i++ ) {
                options += "<option val="+i+">"+i+"</option>";
                document.getElementById('infant').innerHTML = options
                };
        </script>

        <script>
        // function will work after selecting Adult oninput="myFunction()"
            function myFunction(){

                // getting adult, child and infant values
                var adult = document.getElementById("adult").value;
                var child_val = document.getElementById("child").value;
                var infant_val = document.getElementById("infant").value;

                var total = parseInt(adult) + parseInt(child_val);
                console.log("sum of child and adult is:",total);

                // string to integer
                var chd = parseInt(child_val);
                var adl = parseInt(adult);
                var inf = parseInt(infant_val);

                // condition to keep child selected value when adult+child doesn't get more than 9
                if (chd == 0){
                    child(adult)
                    };

                if (chd !== 0 && (adl+chd)>9){
                    child(adult)
                    };

                if (chd !== 0 && (adl+chd)<=9){
                    child(adult);
                    document.getElementById("child").selectedIndex = child_val
                    };

                // condition to keep infant selected value when adult is not less then infant
                if (inf == 0){
                    infant(adult)
                    };

                if ((inf !== 0) && (adl<inf)){
                    infant(adult);
                    console.log(adult, child_val, infant_val)
                    };

                if (inf !== 0 && adl>=inf){
                    infant(adult);
                    document.getElementById("infant").selectedIndex = infant_val;
                    };
                console.log("----", adult, child_val, infant_val)
             }
        </script>

        <script>
        // Child max option update after changing adult
            function child(adult){
                var options = "";
                for (var i = 0; i<(10-parseInt(adult)); i++ ) {
                    options += "<option val="+i+">"+i+"</option>";
                    document.getElementById('child').innerHTML = options
                };
            }
        </script>
        <script>
        // infant max option update after changing adult
             function infant(adult){
                var options_i = "";
                for (var i = 0; i<(1 + parseInt(adult)); i++ ) {
                    options_i += "<option val="+i+">"+i+"</option>";
                    document.getElementById('infant').innerHTML = options_i;
                }
            }
        </script>