
$(function () {
    $('#btn-create').click(function () {
      $('.modal__bg, .modal__contents-type--create').fadeIn(150);
    });
    $('.modal__bg, #btn-close, #close-icon').click(function () {
      $('.modal__bg, .modal__contents-type--create').fadeOut(150);
    });
  });