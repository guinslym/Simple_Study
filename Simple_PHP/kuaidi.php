<?php
header('Content-Type:text/html;charset=utf-8');
$sn=$_GET['sn'];
if (empty($sn)) {
  echo('订单号不能为空');
  exit();
}
$sn=addslashes($sn);
$url='http://www.kuaidi100.com/autonumber/auto?num='.$sn;
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt ($ch, CURLOPT_HEADER,0);
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 20);
curl_setopt($ch, CURLOPT_TIMEOUT, 20);
$response=curl_exec($ch);
$response=json_decode($response);
$companytype=array();
foreach ($response as $key => $value) {
  $companytype[$key]['comcode']=$value->comCode;
}
$comCode = $companytype[0]['comcode'];
$url="http://www.kuaidi100.com/query?type={$comCode}&postid={$sn}&id=1&valicode=&temp=".rand();
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt ($ch, CURLOPT_HEADER,0);
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
curl_setopt($ch, CURLOPT_TIMEOUT, 30);
$data=curl_exec($ch);
if ($errno=curl_errno($ch)) {
    $error_message = curl_strerror($errno);
    echo "curl error ($errno):\n{$error_message}";
}
$httpcode=curl_getinfo($ch,CURLINFO_HTTP_CODE);
curl_close($ch);
if($httpcode==200){
   echo $data;
}else{
   echo $httpcode;
}