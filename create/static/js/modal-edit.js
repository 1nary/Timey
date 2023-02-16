$(function () {
    $('#btn-edit').click(function () {
      $('.modal__bg, .modal__contents-type--edit').fadeIn(150);
    });
    $('.modal__bg, #btn-close').click(function () {
      $('.modal__bg, .modal__contents-type--edit').fadeOut(150);
    });
  });