<?php


Route::get('/', function () {
    return view('welcome');
});
Route::get('division/{n1}/{n2}',function ($n1,$n2) {
    $resultado=$n1/$n2;
    return compact('resultado');
});