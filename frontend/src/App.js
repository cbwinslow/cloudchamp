import React, { useState, useEffect, useRef } from "react";
import {
  ChakraProvider,
  Box,
  Button,
  Input,
  Textarea,
  HStack,
  VStack,
  Text,
  useToast,
} from "@chakra-ui/react";

function App() {
  const [events, setEvents] = useState([]);
  const wsRef = useRef(null);

  const [code, setCode] = useState("// Write your query or script here");
  const [params, setParams] = useState('{\n  "sport": "basketball"\n}');
  const [workspaceName, setWorkspaceName] = useState("demo");
  const toast = useToast();

  const [chatInput, setChatInput] = useState("");
  const [chat, setChat] = useState([]);
  const [scriptOutput, setScriptOutput] = useState("");

  useEffect(() => {
    wsRef.current = new WebSocket(
      `${window.location.protocol === "https:" ? "wss" : "ws"}://${window.location.hostname}:8080/ws/stream`
    );
    wsRef.current.onmessage = (ev) => {
      setEvents((es) => [...es, JSON.parse(ev.data)]);
    };
    return () => wsRef.current.close();
  }, []);

  const sendChat = async () => {
    setChat((c) => [...c, { role: "user", content: chatInput }]);
    setChatInput("");
    const resp = await fetch("/api/chatbot", {
      method: "POST",
      body: JSON.stringify({ prompt: chatInput }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await resp.json();
    setChat((c) => [...c, { role: "bot", content: data.response }]);
  };

  const runScript = async () => {
    const resp = await fetch("/api/script", {
      method: "POST",
      body: JSON.stringify({ code, params }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await resp.json();
    setScriptOutput(data.result || "");
  };

  const saveWorkspace = async () => {
    await fetch("/api/workspace/save", {
      method: "POST",
      body: JSON.stringify({ name: workspaceName, content: JSON.stringify({ code, params }) }),
      headers: { "Content-Type": "application/json" },
    });
    toast({ title: "Workspace saved", status: "success" });
  };
  const loadWorkspace = async () => {
    const resp = await fetch(`/api/workspace/load?name=${workspaceName}`);
    const data = await resp.json();
    try {
      const ws = JSON.parse(data.content);
      setCode(ws.code ?? "");
      setParams(ws.params ?? "");
      toast({ title: "Workspace loaded", status: "success" });
    } catch {
      toast({ title: "Workspace empty or corrupt", status: "error" });
    }
  };

  return (
    <ChakraProvider>
      <HStack align="start" spacing={4} p={4}>
        <VStack align="stretch" w="180px" spacing={3}>
          <Text fontWeight="bold">Workspace</Text>
          <Input
            placeholder="Workspace name"
            value={workspaceName}
            onChange={(e) => setWorkspaceName(e.target.value)}
          />
          <Button size="sm" onClick={saveWorkspace}>
            Save
          </Button>
          <Button size="sm" onClick={loadWorkspace}>
            Load
          </Button>
        </VStack>
        <VStack align="stretch" flex={1} spacing={3}>
          <Text fontWeight="bold">Script/Query Editor</Text>
          <Textarea
            value={code}
            minH="120px"
            onChange={(e) => setCode(e.target.value)}
            fontFamily="mono"
          />
          <Text fontWeight="bold">Parameters (JSON)</Text>
          <Textarea
            value={params}
            minH="80px"
            onChange={(e) => setParams(e.target.value)}
            fontFamily="mono"
          />
          <Button mt={2} colorScheme="blue" onClick={runScript}>
            Run Script/Query
          </Button>
          <Box bg="gray.100" p={2} minH="40px">
            <Text fontWeight="bold">Output:</Text>
            <Text fontFamily="mono" fontSize="sm">
              {scriptOutput}
            </Text>
          </Box>
        </VStack>
        <VStack align="stretch" w="350px" spacing={3}>
          <Text fontWeight="bold">Live Events</Text>
          <Box bg="gray.100" p={2} h="160px" overflowY="auto">
            {events.slice(-10).map((ev, i) => (
              <Box key={i} fontSize="sm">
                {JSON.stringify(ev)}
              </Box>
            ))}
          </Box>
          <Text fontWeight="bold">Chatbot Assistant</Text>
          <Box bg="gray.50" p={2} h="160px" overflowY="auto">
            {chat.map((msg, i) => (
              <Box key={i} color={msg.role === "user" ? "blue.700" : "green.700"} fontSize="sm">
                <b>{msg.role}:</b> {msg.content}
              </Box>
            ))}
          </Box>
          <HStack>
            <Input
              value={chatInput}
              onChange={(e) => setChatInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendChat()}
              placeholder="Ask the assistant..."
            />
            <Button onClick={sendChat}>Send</Button>
          </HStack>
        </VStack>
      </HStack>
    </ChakraProvider>
  );
}

export default App;