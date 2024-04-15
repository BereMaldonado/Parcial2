var pattern_tel=/^[0-9]{10}?$/;
var pattern_correo=/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}?$/;
var pattern_nom=/^[a-zA-Z]{3,30}?$/;
var pattern_ncom=/^[a-zA-Z]{10,50}?$/;
var pattern_curp=/^[a-zA-Z]{4}(\d{6})(([a-zA-Z0-9]){3})?$/;

let valida_forma = () => {
    let js_ncom=getTextInputById("t_nombrecom");
    let js_curp=getTextInputById("t_curp");
    let js_nom=getTextInputById("t_nombre");
    let js_pat=getTextInputById("t_paterno");
    let js_mat=getTextInputById("t_materno");
    let js_tel=getTextInputById("t_telefono");
    let js_cel=getTextInputById("t_celular")
    let js_ema=getTextInputById("t_correo");
    let js_cur=getTextInputById("t_id_curso");
    let js_mun=getTextInputById("t_id_municipio");
    let js_asu=getTextInputById("t_id_asunto");

    if (js_ncom.length <= 0){
        mensaje('error','Error en Nombre Completo', 'El campo de Nombre Completo es obligatorio','')
       return false;
    }
    else if(!pattern_nom.test(js_ncom)){
        mensaje('error','Error en Nombre Completo','El campo Nombre Completo debe tener minimo 10 caracteres','')
        return false;
    }

    else if (js_curp <=0){
        mensaje('error','Error en CURP','El campo de CURP es obligatorio', '')
        return false;
    }
    else if(!pattern_curp.test(js_curp)){
        mensaje('error','Error en CURP','El CURP no cumple el formato ejemplo:PETD740712HZ2','')
        return false;
    }

    else if(js_nom.length <= 0){
        mensaje('error','Error en nombre','El campo Nombre es obligatorio','')
        return false;
    }

    else if(js_pat.length <=0){
        mensaje('error','Error en paterno','El campo Apellido Paterno es obligatorio','')
        return false;
    }

    else if(js_mat.length <=0){
        mensaje('error','Error en Materno','El campo Apellido Materno es obligatorio','')
        return false;
    }

    else if(!pattern_nom.test(js_ncom)||!pattern_nom.test(js_nom) || !pattern_nom.test(js_pat) || !pattern_nom.test(js_mat)){
        mensaje('error','Error en DATOS NOMBRE','El campo Nombre, Apellido Paterno y apellido Materno debe tener minimo 3 caracteres','')
        return false;
    }

    else if(js_tel.length <= 0){
        mensaje('error','Error en Telefono','El campo Telefono es obligatorio','')
        return false;
    }
    else if(!pattern_tel.test(js_tel)) {
        mensaje('error','Error en Telefono','El campo Telefono deben ser solo numeros y deben ser 10 chars','')
        return false;
    }

    else if(js_cel.length <= 0){
        mensaje('error','Error en Celular','El campo Celular es obligatorio','')
        return false;
    }
    else if(!pattern_tel.test(js_cel)) {
        mensaje('error','Error en Celular','El campo Celular deben ser solo numeros y deben ser 10 chars','')
        return false;
    }

    else if(js_ema.length <= 0){
        mensaje('error','Error en Correo','El campo correo es obligatorio','')
        return false;
    }
    else if (!pattern_correo.test(js_ema)) {
        mensaje('error','Error en Correo','El campo Correo no cumple el formato','')
        return false;
    }

    else if (js_cur == "0") {
        mensaje('error','Error en Curso','El campo Curso es obligatorio','')
        return false;
    }   

    else if (js_mun == "0") {
        mensaje('error','Error en Municipio','El campo Curso es obligatorio','')
        return false;
    }  

    else if (js_asu == "0") {
        mensaje('error','Error en Asunto','El campo Curso es obligatorio','')
        return false;
    }  
}

let getTextInputById = (id) => {
    return document.getElementById(id).value.trim();
}
 
let mensaje = (tipo,titulo,texto,liga) => {
    Swal.fire({
        type:tipo,
        title:titulo,
        text: texto,
        footer: liga
      });
}