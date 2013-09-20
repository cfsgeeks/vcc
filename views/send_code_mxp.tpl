<Command>
	% for number in code:
<DTMFSend>
	<Value>{{number}}</Value>
</DTMFSend>
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
</Command>