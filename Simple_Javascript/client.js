function getHost(){
    var domain = document.location.host;
    if (domain.indexOf('www.')==0){
        domain = domain.replace('www.','');
    }
    return domain;
}