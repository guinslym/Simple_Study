function Message (subject,recipient,content) {
	this.subject = subject;
	this.recipient = recipient;
	this.content = content;
}

Message.prototype ={
	constructor:Message,
	sendMessage:function(){
		console.log("Sending message to "+ this.recipient);
	},
	show:function(){
		console.log('To:'+this.recipient+','+"subject:"+this.subject+','+"Message:"+this.content);
	}
};