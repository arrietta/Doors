


let main_data = get_data;
let data

door_type = 'Classic';
let input= {}
let collection ='';
let types = {
  'collection': [],
  'shape': {'icon':[],'shape':[]},
  'portal': [],
  'bevel': [],
  'molding': [],
};
colors= ['989ea1','f1ece1', 'e3d9c6', 'c8c8c7', 'c7c8cc', '52595d', 'eae2d7', 'ecece7', 'd2d3cd', '373c3f', '91583f', 'fb8989', '979392']
const local = 'http://localhost:8000/media/'

function clear(){
    types = {
      'collection': [],
      'icon': [],
      'shape': [],
      'portal': [],
      'bevel': [],
      'molding': [],
    };

    // $("#select_portal").empty();

    $("#select_bevel").empty();
    $("#select_shape").empty();
    $("#select_molding").empty();
    $("#select_portal").empty();


}
colors.forEach(element => add_element('#'+element,'#select_color','color'));
function iterate() {
    main_data = get_data.filter(e => {
        a = e['fields']['collection'].toString().toLowerCase();
        b = collection.toString().toLowerCase();

        return a === b;
    }

);
    clear()
    data = main_data.filter(e => e['fields']['type'] === door_type);
    data.forEach(e => {
        let list = e['fields'];
        for (let el in list) {
            let temp = list[el];
            if (Array.isArray(types[el])&& !types[el].includes(temp)) {

                if(el ==="icon"){
                    let check = true;
                    let i = types['shape'].length;
                    for (let j = 0; j < i; j++) {
                        if(types['shape'][j]['icon'] == temp){
                            check =false;
                        }
                    }
                    if(check){
                        types['shape'][i-1]['icon'] =temp;
                    }


                }else if(el ==="shape"){
                    let check = true;
                    let i = types['shape'].length;
                        for (let j = 0; j < i; j++) {
                            if(types['shape'][j]['shape'] == temp){
                                check =false;

                            }

                        }

                        if(check){
                            types[el].push({'shape':temp});
                            types['shape'][i]['icon'] ='';
                        }


                }else {
                    types[el].push(temp);
                }
            }
        }
    });


    types['bevel'].forEach(element => add_element(element,'#select_bevel','bevel'));
    types['molding'].forEach(element => add_element(element,'#select_molding','molding'));
    types['shape'].forEach(element => add_element(element,'#select_shape','shape'));
    types['portal'].forEach(element => add_element(element,'#select_portal','portal'));
}

iterate();






elements = [];
code = $('#code').attr('value');
function add_element(object, target , type) {
    typee ="'"+type+"'";

    if(type === "color"){
        $(target).append(`<button type="button" style="background-color: ${object}" class=${typee}  onclick="set_value(this,${typee})" value = "${object}"></button>`);
        $('.'+type).addClass('bttn-color');
    }else if(type === "shape"){
         $(target).append(`<button type="button" class=${typee}  onclick="set_value(this,${typee})" value = "${object['shape']}"><img src="media/${object['icon']}"></button>`);
        $('.'+type).addClass('bttn-dark');
    }
    else{
        $(target).append(`<button type="button" class=${typee}  onclick="set_value(this,${typee})" value = "${object}">${object}</button>`);
        $('.'+type).addClass('bttn-dark');
    }

}

function set_value(item , type){
    data = main_data.filter(e => e['fields'][type] === item.value);
    if(type==="color"){
        $('.image_box').css('background-color',item.value);
        $('#color').attr('value',item.value);

    }else{
        iterate()
        set_image('media/'+data[0]['fields']['image'],$('#Door_image'));
        set_image('media/'+data[0]['fields']['portal_image'],$('#portal_image'));
        set_image('media/'+data[0]['fields']['molding_image'],$('#molding_image'));
        $('#price').html(data[0]['fields']['price']);
        $('#door').attr('value',data[0]['pk']);

    }





}

    function set_image(src,link){

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
        }

    }
    window.setInterval(validate, 100);


function changeToCatalogue2(element){
    $('#content-1').hide();
    $('#content-1').addClass('left-move');
    $('#content-2').show();
    $('#content-2').removeClass('right-move');

}
function changeToCatalogue1(element){
    $('#content-1').show();
    $('#content-1').removeClass('left-move');
    $('#content-2').hide();
    $('#content-2').addClass('right-move');
}

$(document).ready(function(){
    $(".c2").click(function(){
        $(".c1").css("color", "grey");
        $(this).css("color", "white");
    });
});
$(document).ready(function(){
    $('.construct').fadeOut();
    $(".c1").click(function(){
        $(".c2").css("color", "grey");
        $(this).css("color", "white");
    });
});

function set_type(type){
    door_type = type;
    iterate()
}

function choose(obj){

    $("span").css("display", "none");
    $('.construct').addClass("unzoom")
    $('.construct').fadeIn();
    setTimeout(open(obj),800);



}
function open(obj){
    $(obj).fadeIn();

    setTimeout(function(){$(".contents").addClass("zoom");$('.construct').removeClass("unzoom");$(".contents").fadeOut();},100);
    setTimeout(function(){

        collection = $(obj).html();

        $('#collection').html(collection);
        $('.catalog').fadeOut();
        iterate();
    },200);

}