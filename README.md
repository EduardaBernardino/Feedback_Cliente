<h1 align="center">📩 Pós-venda Automático – Coleta de Feedback de Clientes</h1>

Um projeto simples, mas poderoso, desenvolvido em **Python**, que automatiza o processo de **pós-venda**.  
Após a conclusão de uma venda, o sistema envia um e-mail personalizado ao cliente pedindo feedback sobre a experiência de compra — ajudando a equipe de marketing e vendas a coletar **insights reais** sobre o atendimento e a satisfação do cliente.

---

### **Funcionalidades**
✅ Leitura automática de um arquivo CSV com os dados das vendas.  
✅ Envio de e-mails personalizados após a entrega.  
✅ Mensagens em **HTML e texto**, prontas para uso corporativo.  
✅ Compatível com **Gmail (SMTP + Senha de App)**.  
✅ Código simples, seguro e de fácil personalização.  

---

### **Estrutura do Projeto**
📁 post_venda/
├── post_venda.py # Script principal
├── sales.csv # Lista de vendas (nome, email, pedido, data)
├── README.md 


---

### **📨 Exemplo de e-mail enviado**
**Assunto:** Como foi sua experiência com a Empresa X?

Olá Maria,  
Esperamos que esteja tudo certo com o seu pedido **BS1234** 😊  

Você poderia avaliar sua experiência com nosso atendimento?  

👉 **Avaliar Atendimento**  

Obrigado!  
Equipe **Empresa X**

---

### **🧑‍💻 Tecnologias utilizadas**
- **Python 3.10+**  
- **smtplib / email.message**  
- **ssl**  
- **csv / datetime**  
- **dotenv** (para segurança de credenciais)
