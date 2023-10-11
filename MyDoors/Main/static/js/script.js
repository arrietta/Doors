


        data['shapes'].forEach(element => add_element(element,'#select_shape','shape'));
        data['portals'].forEach(element => add_element(element,'#select_portal','portal'));
        data['bevels'].forEach(element => add_element(element,'#select_bevel','bevel'));
        data['moldings'].forEach(element => add_element(element,'#select_molding','molding'));
        data['color'].forEach(element => add_element(element,'#select_color','color'));

        let shape;
        let portal;
        let bevel;
        let molding;
        let color;

        function add_element(object, target , type){
            type = '"'+type+'"';
            console.log(type);
            $(target).append('<button type="button" onclick="set_value(this,'+type+')" ' +
                'value = "' + object['id'] + '">' + object['name'] + '</button>');
        }
        function set_value(object , type){
            switch (type) {
                case 'shape':
                    shape = object;
                    break;
                case 'portal':
                    portal = object;
                    break;
                case 'bevel':
                    bevel = object;
                    break;
                case 'molding':
                    molding = object;
                    break;
                case 'color':
                    color = object;
                    break;
            }
            $('#'+type).attr('value' , object);
                console.log("#"+type);
        }
