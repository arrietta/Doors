    const data = get_data;
    data['shapes'].forEach(element => add_element(element,'#select_shape','shape'));
    data['portals'].forEach(element => add_element(element,'#select_portal','portal'));
    data['bevels'].forEach(element => add_element(element,'#select_bevel','bevel'));
    data['moldings'].forEach(element => add_element(element,'#select_molding','molding'));
    data['color'].forEach(element => add_element(element,'#select_color','color'));
    doors = data['door'];
    elements = [];
    code = $('#code').attr('value');
    function add_element(object, target , type) {
        typee ="'"+type+"'";
        $(target).append(`<button type="button" class=${typee} id = "type_${object['id']}" onclick="set_value(this,${typee})" value = "${object['id']}">${object['name']}</button>`);
        if(typee !== "'"+'shape'+"'"){
            $(target).hide();
        }
        $('.'+type).addClass('butn-light');
    }
    function shuffle(array) {
        let currentIndex = array.length,  randomIndex;
        while (currentIndex > 0) {
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex--;
            [array[currentIndex], array[randomIndex]] = [
              array[randomIndex], array[currentIndex]];
          }

          return array;
    }
    function set_value(object , type){
        const set = {'shape': 'portal', 'portal': 'bevel', 'bevel': 'molding','molding':'color'};
        const list = {'shape':['portal','bevel','molding','color'], 'portal': ['bevel','molding','color'], 'bevel': ['molding','color'],'molding':['color']}
        if(type !== 'color'){
            list[type].forEach(element =>{
                $('#select_'+element).hide();
                elements[element] = null;
            });
        }

        $('#select_'+set[type]).fadeIn()
        if(type !== 'molding' && type !== 'color'){
            show_element(set[type]);
            data[set[type]+'s'].forEach(element =>hide_element(element,set[type],type,object.innerHTML));
        }

        elements[type] = object.innerHTML;
        let door = doors.filter(Filtering);
        door = shuffle(door);
        door.forEach(element => {
            if(elements[type] === element[type]){
                set_image(element['image']);
                $('#door').attr('value',element['id']);
            }
        });
    }
    function Filtering(element){
        const list = ['shape','portal','bevel','molding'];
        let res;
        list.forEach(e => {
            if(elements[e]){
                res = element[e] === elements[e];
            }
        });
        return res;
    }
    function hide_element(array, target,type, arg){
        if(array[type] !== arg){
            $("." + target+"[value='"+array['id']+"']").hide();
        }
    }
    function show_element(target){
        $("." + target).show();
    }
    function set_image(src){
        let link = $('#Door_image');
        if(link.attr("src").toString() !== src.toString()){
            link.hide();
            link.attr('src',src);
            link.fadeIn();
        }
    }
    function validate(){
        const object = $("#code");
        if(object.attr('value')!==code){
            object.attr('value',code);
            console.log('asd')
        }

    }
    window.setInterval(validate, 100);

