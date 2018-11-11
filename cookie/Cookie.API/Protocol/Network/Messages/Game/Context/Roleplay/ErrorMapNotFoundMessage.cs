﻿using Cookie.API.Utils.IO;

namespace Cookie.API.Protocol.Network.Messages.Game.Context.Roleplay
{
    public class ErrorMapNotFoundMessage : NetworkMessage
    {
        public const ushort ProtocolId = 6197;

        public ErrorMapNotFoundMessage(int mapId)
        {
            MapId = mapId;
        }

        public ErrorMapNotFoundMessage()
        {
        }

        public override ushort MessageID => ProtocolId;
        public int MapId { get; set; }

        public override void Serialize(IDataWriter writer)
        {
            writer.WriteInt(MapId);
        }

        public override void Deserialize(IDataReader reader)
        {
            MapId = reader.ReadInt();
        }
    }
}