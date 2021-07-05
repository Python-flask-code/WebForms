## WebForms
Web sayfasında bir form arayüzü.
Bu form arayüzünü oluştururken Flask get-post yapılarını kullandım. Aynı zamanda Inheritance yapısını kullandım. Layout class'ım ana class 'ım oldu diğer html class'ları bu ana class' tan miras aldılar. Bu şekilde tekrar tekrar aynı code'ları yazma zorunluluğundan kurtuldum ve code karmaşasını önlemiş oldum.
# Inheritance
Inheritance Türkçe karşılığı kalıtım veya miras alma olan bu kavram nesne tabanlı programlama(OOP) ile gelen bir kavramdır. Burada  biz html sayfalarını miras alacağız.
Kullanımı --> {% extends “miras_alinacak_dosyaAdi.html” %} 
Mirası aldığımız sayfaya gelerek en üste bu code ' u yazarsanız . Miras alma işlemini halletmiş oluyoruz. Peki miras alma yaptıktan sonra değişiklik yapmak istersek ne yapacağız ?
Block yapısını kullanacağız. Blocklar miras aldığımız bir sayfa üzerinde değişiklik yapmak istediğimiz zaman kullanacağımız ifadedir.
{% block block_adi %}
    ……….
{% endblock %} bu şekilde hem miras alınan yerde hemde miras alıcağımız yerde kullanırsak block içerisindeki kısmı değiştirerek miras alma işlemini gerçekleştirmiş oluyoruz .
