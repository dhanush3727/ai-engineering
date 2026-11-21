// Implementation details, make this private
const conversations = new Map<string, string>();

// Export the public interface
export const conversationRepo = {
   getLastResponseId(conversationId: string) {
      return conversations.get(conversationId);
   },
   setLastResponseId(conversationId: string, responseId: string) {
      return conversations.set(conversationId, responseId);
   },
};
