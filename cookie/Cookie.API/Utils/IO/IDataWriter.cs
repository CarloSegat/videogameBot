using System;

namespace Cookie.API.Utils.IO
{
    public interface IDataWriter : IDisposable
    {
        byte[] Data { get; }

        int Position { get; }

        void WriteShort(short @short);

        void WriteInt(int @int);

        void WriteLong(long @long);

        void WriteUShort(ushort @ushort);

        void WriteUInt(uint @uint);

        void WriteULong(ulong @ulong);

        void WriteByte(byte @byte);

        void WriteSByte(sbyte @byte);

        void WriteFloat(float @float);

        void WriteBoolean(bool @bool);

        void WriteChar(char @char);

        void WriteDouble(double @double);

        void WriteSingle(float single);

        void WriteUTF(string str);

        void WriteUTFBytes(string str);

        void WriteBytes(byte[] data);

        void Clear();

        void Seek(int offset);

        void WriteVarInt(int value);

        void WriteVarUhInt(uint value);

        void WriteVarShort(short value);

        void WriteVarUhShort(ushort value);

        void WriteVarLong(long value);

        void WriteVarUhLong(ulong value);
    }
}