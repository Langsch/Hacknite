// pede confirmacao antes de enviar formularios marcados com data-confirmar="mensagem"
document.addEventListener('submit', (evento) => {
  const form = evento.target;
  if (form.dataset.confirmar && !confirm(form.dataset.confirmar)) {
    evento.preventDefault();
  }
});
